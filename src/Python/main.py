import ingestData as ingest
import createPostcodeMap as map
import getDecileDataByPostcode as getDecileData
import visualiseData as vis
import analyseData as analyse

def main(centroidsFile, iodFile):
        print("Application loading...")
        print("Loading data...")
        ingestData = ingest.IngestData(centroidsFile, iodFile)
        centroidsDF = ingestData.readCentroidsMap()
        iodDF = ingestData.readIndicesOfDeprivation()
        print("Mapping LSOA data to postcodes...")
        map_data = map.getPostcodeData(centroidsDF, iodDF)
        postcodeMapRef = map_data.createPostcodeMap()
        analyseData = analyse.AnalyseData(postcodeMapRef)
        analyseData.exploratoryAnalysis()
        return postcodeMapRef
     

if __name__ == "__main__":
        main('C:\\Users\\matth\\MyScripts\\temp\\ONSPD_Centroids.csv.gz', 'C:\\Users\\matth\\MyScripts\\temp\\IoD2019.csv.gz') #calls the main function
    