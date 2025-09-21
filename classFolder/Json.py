import json

class Json:

    @staticmethod
    def read(path :str):

        fileJson = None
        objOut = None

        try:
            fileJson = open(path, "r")
            strJson = fileJson.read()
            objOut = json.loads(strJson)
        except Exception as e:
            print(e)
        finally:
            if(fileJson != None and not fileJson.closed):
                fileJson.close()
            else:
                raise Exception("error ro read file json.")

        return objOut


    @staticmethod
    def write(path :str, objToWrite):

        fileJson = None
        isSuccess = True

        try:
            fileJson = open(path, "w")
            json.dump(objToWrite, fileJson, indent=4)
        except Exception as e:
            print(e)
            isSuccess = False
        finally:
            if(fileJson != None and not fileJson.closed):
                fileJson.close()
            else:
                raise Exception("error ro read file json.")

        return isSuccess

        
