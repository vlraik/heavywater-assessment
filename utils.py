import joblib
import urllib
class FlaskUtil:
    """
    This class is used to process the requests from the client.
    """

    def __init__(self):
        """
        Initialize the models so that it doesn't take time to load everytime.
        """
        self.model = Model()
        self.load_model = self.model.load_model()


    def get_data(self, request):
        """
        parse the data sent by the client.
        :param request:
        :return: data
        """
        data = None
        if request.method == 'GET':
            if 'words' in request.form:
                data = request.form['words']
        elif request.method == 'POST':
            if 'words' in request.form:
                if request.form is not None:
                    data = request.form['words']
        return data

    def predictions(self, data):
        """
        use the trained model to get the results.
        :param data:
        :return: dict for prediction and confidence values
        """

        pred = list(self.load_model.predict([data]))[0]
        likelihood = 100 * self.load_model.predict_proba([data]).max()
        return {'prediction': pred, 'confidence': likelihood}


class Model:
    """
    This class is used for loading the trained model
    """

    def __init__(self):
        self.pred_model = None

    def load_model(self):
        """
        We are accessing S3 buckets to get the pickle file in which the model is saved.
        :return: trained model
        """
        if self.pred_model == None:
            #temp = open('model_4.pkl', 'rb')

            myurl = "https://heavywater.s3.us-east-2.amazonaws.com/model_4.pkl"
            temp = urllib.request.urlopen(myurl)
            self.pred_model = joblib.load(temp)
        return self.pred_model
