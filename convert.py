import json
import re
import os


def getAllCode(direcoryPath):

    code_map = {}
    for root, dirs, files in os.walk(direcoryPath):
        for file_name in files:
            if file_name.endswith('.sol'):
                file_path = os.path.join(root, file_name)
                code_map[file_name[:file_name.rfind('.')]] = getCode(file_path)
    return code_map

def getCode(filePath):
    with open(filePath, 'r', encoding='utf-8') as file:
        file_content = file.read()
        return  file_content

def getCorpusMap(filePath,test_cases_map):
    with open(filePath, 'r', encoding='utf-8') as file:
        data = file.read().strip()
        modified_data = '[' + data.replace('\n', ',') + ']'


    # test_cases_map = {}
    modified_data_list = json.loads(modified_data)
    for test_case in modified_data_list:
        data_readable = test_case.get('data_readable')
        if data_readable is None:
            continue
        function_name = re.match(r'[^\W_]+', data_readable).group()
        test_cases_map[function_name] = json.dumps(test_case)

    for key, value in test_cases_map.items():
        print(f"Key: {key}")
        print(f"Value: {value}")
        print()
    return test_cases_map

def getAllCorpusMap(directoryPath):
    replayable_files = []
    for root, dirs, files in os.walk(directoryPath):
        for file in files:
            if file.endswith("replayable"):
                replayable_files.append(os.path.join(root, file))

    test_cases_map = {}
    for filePath in replayable_files:
        test_cases_map = getCorpusMap(filePath,test_cases_map)

    return test_cases_map

def getAllMap(directoryPath):
    subfolders = [f.path for f in os.scandir(directoryPath) if f.is_dir()]
    subfolder_names = [f.name for f in os.scandir(directoryPath) if f.is_dir()]

    allMap = {}
    for name, path in zip(subfolder_names, subfolders):
        test_cases_map = getAllCorpusMap(path)
        allMap[name] = test_cases_map

    print("======allMap")
    for x in allMap:
        print(x)
        print("============================================")
        print(allMap[x])
        print("============================================")

    return allMap


    with open(r'E:\ityfuzz\ityfuzz\backup\inicorpus\AETH\2_seed_replayable', 'r') as file:
        data = json.load(file)

    data_readable = data.get('data_readable', '')


    function_name = re.match(r'[^\W_]+', data_readable).group()




def combineText(code,initialText):
    return code+"\n"+initialText


def getInitialText():
    with open(r'E:\ityfuzz\ityfuzz\test.txt', 'r', encoding='utf-8') as file:
        file_content = file.read()
    return file_content

def getAllInitialTextMap(codeMap,initialText):
    AllInitialTextMap = {}
    for name,code in codeMap.items():
        AllInitialTextMap[name] = combineText(code,initialText)
    return AllInitialTextMap

def getExampleQuestionText():
    with open(r'E:\ityfuzz\ityfuzz\exampleQuestion.txt', 'r', encoding='utf-8') as file:
        file_content = file.read()
    return file_content

def getExampleAnswerText():
    with open(r'E:\ityfuzz\ityfuzz\ExampleAnswer.txt', 'r', encoding='utf-8') as file:
        file_content = file.read()
    return file_content

def writeCprpusByResponseMapAndCorpusMap(ResponseMap,CorpusMap):
    for contractName,childMap in corpusMap:
        for methodName,corpusList in childMap:
            for responseContractName,responseCorpus in ResponseMap:
                1==1

def convertResponseToCorpus(corpus,respone):
    return

def convert(corpusMap,resultTxt):
    data = json.loads(resultTxt)

    allList = []
    for test_case in data:

        childList = []
        index = test_case.get("number")
        for operation in test_case.get("operator"):
            function_namen = operation.get("function")
            param = operation.get("parameter")

            if function_namen not in corpusMap:
                continue
            corpus = corpusMap[function_namen]
            parsed_data = json.loads(corpus)
            try:
                data_list = parsed_data["data"]["b"]["data"]
            except KeyError:
                childList.append(corpus)
                continue
            i = 0
            for item in data_list:
                if i >= len(test_case):
                    break
                print("==========================")
                print(parsed_data)
                print(index)
                print(function_namen)
                print(item)
                print("==========================")
                if isinstance(param[i], str):
                    print("if=======")
                    print([int(param[i][j:j + 2], 16) for j in range(2, len(param[i]), 2)])
                    print(item["b"]["data"])
                    item["b"]["data"] = [int(param[i][j:j + 2], 16) for j in range(2, len(param[i]), 2)]
                else:
                    print("else========")
                    print(param[i])
                    print(item["b"]["data"])
                    item["b"]["data"] = convert_to_list(param[i])
                i = i + 1


            childList.append(json.dumps(parsed_data))
        allList.append(childList)
    return allList

def convert_to_list(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")

    hex_str = hex(num)[2:]

    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str
    half_len = len(hex_str) // 2
    result_list = [int(hex_str[i:i + 2], 16) for i in range(0, len(hex_str), 2)]

    return result_list


    print("corpusList size===============")
    print(len(corpusMap))
    print(corpusMap)
    time = 0;
    parsed_dataList = []
    while (time < len(corpusMap)):
        print(time)
        values_list = list(corpusMap.values())
        corpus = values_list[time]
        time = time + 1
        modified_data_list = json.loads(corpus)
        data_readable = modified_data_list.get('data_readable')
        if data_readable is None:
            continue
        function_name = re.match(r'[^\W_]+', data_readable).group()


        data = json.loads(resultTxt)
        for test_case in data:
            index = test_case.get("number")
            for operation in test_case.get("operator"):
                function_namen = operation.get("function")
                param = operation.get("parameter")

                if(function_name == function_namen):

                    i = 0;
                    parsed_data = json.loads(corpus)

                    stack = [parsed_data]
                    while stack:
                        current_obj = stack.pop()
                        if isinstance(current_obj, dict):
                            for key, value in current_obj.items():
                                if key == 'type' and value == 'A256':
                                    if isinstance(param[i], str):
                                        print("param",param[i])
                                        print("i",i)
                                        current_obj['data'] = str([int(param[i][j:j + 2], 16) for j in range(2, len(param[i]), 2)])
                                    else:
                                        current_obj['data'] = str(param[i])
                                    i = i+1
                                    parsed_dataList.append(parsed_data)
                                    time = 0

                                elif isinstance(value, (dict, list)):
                                    stack.append(value)
                        elif isinstance(current_obj, list):
                            for item in current_obj:
                                stack.append(item)


                    for key, value in parsed_data.items():
                        if key == "data":
                            for key2, value2 in parsed_data.get(key):
                                print(key2)
                                print("=======")
                                print(value2)
                                if key == "type" and value == "A256":
                                    if isinstance(param[i], str):
                                        parsed_data["data"] = str([int(param[i][i:i+2], 16) for i in range(2, len(param[i]), 2)])
                                    else:
                                        parsed_data["data"] = str(param[i])
                                    parsed_dataList.append(parsed_data)
                                    time = 0
    return parsed_dataList


def convertResponseFileToCorpus(resourseFolder,destinationFolder,corpusMap):
    code_map = {}
    for root, dirs, files in os.walk(resourseFolder):
        for file_name in files:
            if file_name.endswith('.txt'):
                num = 0
                file_path = os.path.join(root, file_name)
                resultFile = getCode(file_path)
                for contractName,corpusMapChild in corpusMap.items():
                    if(contractName == file_name[:file_name.rfind('.')]):
                        backjson = convert(corpusMapChild,resultFile)
                        file_folder_path = os.path.join(destinationFolder, contractName)
                        singlefilepath = os.path.join(file_folder_path, str(num))
                        print(len(backjson[2]))

                        for parsed_data in backjson:
                            singlefilepath = os.path.join(file_folder_path, str(num))
                            for child in parsed_data:
                                json_string = child

                                with open(singlefilepath, "a") as output_file:
                                    output_file.write(json_string)
                                    output_file.write("\n")

                            num = num + 1


codeMap = getAllCode(r'E:\ityfuzz\ityfuzz\backup\contract')
# getCorpusMap(r'E:\ityfuzz\ityfuzz\backup\inicorpus\AETH\12_replayable')
corpusMap = getAllMap(r'E:\ityfuzz\ityfuzz\backup\inicorpus')
initialText = getInitialText()
AllInitialTextMap = getAllInitialTextMap(codeMap,initialText)
convertResponseFileToCorpus(r'E:\ityfuzz\ityfuzz\backup\GPT3.5result1',r'E:\ityfuzz\ityfuzz\backup\GPT3.5result1test',corpusMap)
exampleQuestionText = getExampleQuestionText()
exampleAnswerText = getExampleAnswerText()
for i,j in resultMap.items():
    print("============name==============")
    print(i)
    print("============name==============")
    print("============result==============")
    print(j)
    print("============result==============")
