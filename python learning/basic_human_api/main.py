from text_clean import clean_text;
from textAnalysis import analysisMessage;
from apiCall import aipResponce;



def Main():
    message = " How to get connectin i DB ";

    clearmgs = clean_text(message);

    analysisResponce  = analysisMessage(clearmgs);

    result = aipResponce(analysisResponce); 

    return result;

responce  = Main();

print(responce);




