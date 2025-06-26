import ee
import geemap
import datetime
import os
import ollama
clientID =  '7682362737-sbrre3pn00vk7nfngujou7jmil5eqpes.apps.googleusercontent.com'
ee.Authenticate(auth_mode=locals,quiet=True)
ee.Initialize(project="learning-project-436517")
print(ee.String("ee, imported, auth complete").getInfo())


Ukraine = {
    "geodesic": false,
    "type": "Polygon",
    "coordinates": [[[
        23.32989305133208, 46.18192421358463],
        [38.66680711383208, 46.18192421358463],
        [38.66680711383208, 52.081364449517274],
        [23.32989305133208, 52.081364449517274],
        [23.32989305133208, 46.18192421358463]]]};
Mariupol = {
    "geodesic": false,
    "type": "Polygon",
    "coordinates": [[
        [37.57443050213773, 47.08504167310611],
        [37.66575435467679, 47.07709281123811],
        [37.70557979412992, 47.128505634229306],
        [37.65751460858304, 47.152792595141435],
        [37.490659750184605, 47.12943995326131],
        [37.47555354901273, 47.02750256697862],
        [37.57443050213773, 47.08504167310611]]]};
Odesa = {
    "geodesic": false,
    "type": "Polygon",
    "coordinates": [
        [
            [30.598608101814754, 46.34232305677091],
            [30.801855172127254, 46.34232305677091],
            [30.801855172127254, 46.55049603225274],
            [30.598608101814754, 46.55049603225274],
            [30.598608101814754, 46.34232305677091]
        ]
    ]
}
Gaza = {
    "geodesic": false,
    "type": "coordinates",
    "coordinates": [
        [
            [34.281418764703915, 31.161562347574517],
            [34.58766266118829, 31.541541281809828],
            [34.49153229009454, 31.608230377233596],
            [34.20863434087579, 31.327112208340928],
            [34.281418764703915, 31.161562347574517]
        ]
    ]
}

Location = Odesa;

# Centers the Map
#Center = (ee.Geometry.Polygon(Ukraine.coordinates[0])).centroid().coordinates()
#Map.addLayer(ee.Geometry.Polygon(Ukraine.coordinates[0]), {}, "Area of Intrest")
#print(Number(Center.getInfo()[0]));
#Map.setCenter(Number(Center.getInfo()[0]), Number(Center.getInfo()[1]), 12)
ee_date = ee.date()
print(ee_date)
py_date = datetime.datetime.utcfromtimestamp(ee_date.getInfo()["value"]/1000.0)
print(py_date)
Today = newDate()


Past = newDate(Today);

Past1 = new
Date(Today);

Past2 = new
Date(Today);

Past.setDate(Past.getDate() - 10) # The last 14 days from present

Past1.setDate(Past1.getDate() - 50); # Past Date range Beggining
Past2.setDate(Past2.getDate() - 60); # Past Date range End
Past = f"{Past.getFullYear()}-{(Past.getMonth() + 1)}-{Past.getDate()}"
Today = f"{Today.getFullYear()}-{(Today.getMonth() + 1)}-{Today.getDate()}"
Past1 = f"{Past1.getFullYear()}-{(Past1.getMonth() + 1)}-{Past1.getDate()}"
Past2 = f"{Past2.getFullYear()}-{(Past2.getMonth() + 1)}-{Past2.getDate()}"

#Past = Past2
#Today = Past1


for x in range(2):
    # Sat Decleration Area
    Radar = ((ee.ImageCollection('COPERNICUS/S1_GRD').filterDate(Past, Today)
             .filterBounds(Ukraine)
             .filter(ee.Filter.lt("resolution_meters", 13)).select("VV", "VH"))
             .filterBounds(Ukraine));
    S2 = (((((ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
          .filterDate(Past, Today))
          .filterBounds(Ukraine))
          .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 3)))
          .select("SCL"))
          .filterBounds(Ukraine));
    Visual = (((((ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
              .filterDate(Past, Today))
              .filterBounds(Ukraine))
              .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 5)))
              .select("TCI_R", "TCI_G", "TCI_B"))
              .filterBounds(Ukraine));
    Built = ((((ee.ImageCollection("GOOGLE/DYNAMICWORLD/V1")
             .filterDate(Past, Today))
             .filterBounds(Ukraine))
             .select("built"))
             .mosaic().round().toInt());
    print(Radar.getInfo().features[0]);
    #Asending and Desending V / H Band Selection

    VV = Radar.select("VV").mosaic().unitScale(-2, 25).clamp(0, 1); # Some flat feilds show up, minimul
    VH = Radar.select("VH").mosaic().unitScale(-8, 5).clamp(0, 1);
    CombinedRadar = VH.add(VV).updateMask(ee.Geometry(Ukraine));
    # Modifying Sat Data
    S2 = S2.mosaic().unitScale(4, 5).clamp(0, 1).toInt()
    multiPointAssessment = ((CombinedRadar.add(S2).add(Built)).unitScale(2, 3).ceil().clamp(0, 1));
    multiPointAssesment.updateMask(multiPointAssesment.not())

    # Where data is stored in global var
    if not RadarMaskedCurrent:
        RadarMaskedCurrent = CombinedRadar.updateMask(S2).ceil().clamp(0, 1)
        VisualCurrent = Visual
    else:
        RadarMaskedPast = CombinedRadar.updateMask(S2).ceil().clamp(0, 1)
        VisualPast = Visual
    test = S2

#DamageOnly = RadarMaskedCurrent.subtract(RadarMaskedPast);
#DamageOnly = ee.Algorithms.CannyEdgeDetector(DamageOnly.updateMask(DamageOnly), 3.1, 0);
#DamageOnly = ee.Algorithms.CrossCorrelation(RadarMaskedCurrent, RadarMaskedPast, 5, 3, 0.8)
#exportparaMap = {image: RadarMasked, bucket: "learning-project-436517.appspot.com", scale: 10, region: Odesa}
#exportparaImage = {image: RadarMasked, crs: "EPSG:4326", bucket: "learning-project-436517.appspot.com", scale: 10,maxPixels: 8030040147504, region: Odesa}
