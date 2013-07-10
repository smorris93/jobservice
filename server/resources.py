from flask.ext.restful import Resource
from flask.ext.restful.reqparse import RequestParser


class FetchRange(Resource):

    def get(self):
        lRange = FetchRange.sModel.getRange()
        return lRange


class Report(Resource):

    def __init__(self):
        super(Report, self).__init__()
        self.__mParser = RequestParser()
        self.__mParser.add_argument('success', type=str, required=True)
        self.__mParser.add_argument('message', type=str)
        self.__mParser.add_argument('rangeId', type=int, required=True)

    def get(self):
        lArgs = self.__mParser.parse_args()
        lSuccess = lArgs['success']
        lMessage = lArgs['message']
        lRangeId = lArgs['rangeId']
        Report.sModel.report(
            True if lSuccess == "true" else False,
            lRangeId,
            lMessage
        )
        return {}


class Progress(Resource):
    def get(self):
        return {
            'value': Progress.sModel.getProgress(),
            'message': Progress.sModel.getSuccessMessage()
        }


class Reset(Resource):
    def get(self):
        Reset.sModel.reset()
        return {}



