
if __name__ == "__main__":
    exit(1)


from os.path import (
    isfile, isdir
)

import json
from typing import Iterable


class CaseFileError(Exception):
    REASONS: dict[int, str] = {
        1: "\nThe key: {} is not recogniced\nPlease fix the case file befor running again!",
        2: "\nYou must give th case file some nation tags\nPlease give the tags for the nations you want to write!",
        3: "\nThe nation tag: {} is not of the right size\nAll nation tags must be 3 chr long!"
    }

    def __init__(self, invalidKey: str, reason: str):
        self.invKey = invalidKey
        self.reason = reason

    def __str__(self) -> str:
        return self.REASONS.get(self.reason).format(self.invKey)


class CaseFileHandler(object):
    """
    Handles the case file, both reading and validating\n
    """
    VALIDKEYS: dict[str, type] = {
            "basePath": str,
            "targetPath": str,
            "allowPathOcerwrite": bool,
            "force": bool,
            "instruct": dict,
            "nationTag": str,
            "nationCap": int,
            "templateFiles": list,
            "templateOverwritePath": str,
            "targetOverwritePath": str
    }

    def readCaseFile(self, cFile: str) -> dict:
        data: dict = {}
        with open(cFile, 'r') as cf:
            data = json.load(cf.read())

        self._validateCaseFile(data)

        return data


    def _validateCaseFile(self, data: dict) -> None:
        topLayer: Iterable = data.keys()

        for key in topLayer:
            if key not in self.VALIDKEYS:
                raise CaseFileError(key, 1)

        nationTags: (dict) = data.get("instruct")

        if not nationTags:
            raise CaseFileError('', 2)
        
        for tag in nationTags:
            if len(tag) != 3:
                raise CaseFileError(tag, 3)


class ReadWriteFileHandling(object):
    """
    Handles the programs files. Is initialized to look for templates in its locale bin folder,\n
    and too put results in the locale out folder\n
    @param _templatePath: str="./bin"\n
    @param _targetPath: str="./out"\n
    @param _allowPathOverwrite: bool=False
    """

    def __init__(self, _templatePath: str="./bin", _targetPath: str="./out", _allowPathOverwrite: bool=False):
        assert isdir(_templatePath), "The template folder must be an acctual folder!"
        assert isdir(_targetPath), "The target folder must be an acctual folder!"

        self.allowPathOverwrite = _allowPathOverwrite
        self.templatePath = _templatePath
        self.targetPath = _targetPath

    def setTemplatePath(self, _templatePath: str) -> None:
        assert self.allowPathOverwrite, "Your case file does not allow path overwrite"
        assert isdir(_templatePath), "The template folder must be an acctual folder!"

        self.templatePath = _templatePath
        return

    def setTargetPath(self, _targetPath: str) -> None:
        assert self.allowPathOverwrite, "Your case file does not allow path overwrite"
        assert isdir(_targetPath), "The target folder must be an acctual folder!"

        self.targetPath = _targetPath
        return

    def readTemplateFile(self, rfile: str) -> dict:
        assert False, "not implemneted"

    def writeFile(self, wfile: str) -> None:
        assert False, "not implemneted"

