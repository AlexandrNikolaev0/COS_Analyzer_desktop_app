String cmdTxt = "";
String statusTxt = "";
#include <ArduinoJson.h>
DynamicJsonDocument outputInfo(256);
DynamicJsonDocument inputMsg(1024);
String jsonParseAndProcess(String str)
{
  inputMsg.clear();
  deserializeJson(inputMsg, str);


  if (inputMsg.containsKey("cmd"))
  {
    cmdTxt = inputMsg["cmd"].as<String>();
    if (cmdTxt == "get_status") {
      
      outputInfo.clear();
      outputInfo["status"] = 1;
      String outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);
      return "Success";
    }

    if (cmdTxt == "auth") {
      String login = inputMsg["login"].as<String>();
      String password = inputMsg["password"].as<String>();
      
      outputInfo.clear();
      if (login == "Analyst" || (login == "Lab Manager" && password == "123"))
      {
        outputInfo["status"] = 1;
      }
      else
      {
        outputInfo["status"] = 0;
      }
      String outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);
      return "Success";
    }

    if (cmdTxt == "get_devicesStatus") {


      
      outputInfo.clear();
      outputInfo["device"] = "Controller";
      outputInfo["color"] = "green";
      String outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      outputInfo.clear();
      outputInfo["device"] = "innerTemp";
      outputInfo["color"] = "yellow";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);



      outputInfo.clear();
      outputInfo["device"] = "outerTemp";
      outputInfo["color"] = "yellow";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);



      outputInfo.clear();
      outputInfo["device"] = "cellTemp";
      outputInfo["color"] = "yellow";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);



      outputInfo.clear();
      outputInfo["device"] = "sampler";
      outputInfo["color"] = "yellow";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);



      outputInfo.clear();
      outputInfo["device"] = "CLMeter";
      outputInfo["color"] = "green";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      outputInfo.clear();
      outputInfo["finish"] = "finish";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      ////
      outputInfo.clear();
      outputInfo["device"] = "Controller";
      outputInfo["color"] = "green";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      outputInfo.clear();
      outputInfo["device"] = "innerTemp";
      outputInfo["color"] = "green";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);



      outputInfo.clear();
      outputInfo["device"] = "outerTemp";
      outputInfo["color"] = "green";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);



      outputInfo.clear();
      outputInfo["device"] = "cellTemp";
      outputInfo["color"] = "green";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);



      outputInfo.clear();
      outputInfo["device"] = "sampler";
      outputInfo["color"] = "green";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      outputInfo.clear();
      outputInfo["device"] = "CLMeter";
      outputInfo["color"] = "green";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);

      outputInfo.clear();
      outputInfo["finish"] = "finish";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);

      ///

      outputInfo.clear();
      outputInfo["device"] = "Controller";
      outputInfo["color"] = "blue";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      outputInfo.clear();
      outputInfo["device"] = "innerTemp";
      outputInfo["color"] = "blue";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      outputInfo.clear();
      outputInfo["device"] = "outerTemp";
      outputInfo["color"] = "blue";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      outputInfo.clear();
      outputInfo["device"] = "cellTemp";
      outputInfo["color"] = "blue";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      outputInfo.clear();
      outputInfo["device"] = "sampler";
      outputInfo["color"] = "blue";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      outputInfo.clear();
      outputInfo["device"] = "CLMeter";
      outputInfo["color"] = "blue";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);

      outputInfo.clear();
      outputInfo["finish"] = "finish";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);




      ///

      outputInfo.clear();
      outputInfo["device"] = "Controller";
      outputInfo["color"] = "red";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      outputInfo.clear();
      outputInfo["device"] = "innerTemp";
      outputInfo["color"] = "red";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);



      outputInfo.clear();
      outputInfo["device"] = "outerTemp";
      outputInfo["color"] = "red";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      outputInfo.clear();
      outputInfo["device"] = "cellTemp";
      outputInfo["color"] = "red";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);



      outputInfo.clear();
      outputInfo["device"] = "sampler";
      outputInfo["color"] = "red";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      outputInfo.clear();
      outputInfo["device"] = "CLMeter";
      outputInfo["color"] = "red";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);

      outputInfo.clear();
      outputInfo["finish"] = "finish";
      outputString = "";
      serializeJson(outputInfo, outputString);
      sendSerialMessage(outputString);


      return "Success";

    }


  }

  return "Json is incorrect";
}


//Sends message object via Serial or Serial Bluetooth.
void sendSerialMessage(String message) {
  Serial.print(message);
  Serial.print("\n");
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Commands recieving
  String str = "";
  char ch = 0;
  int len = 0;

  while (Serial.available())
  {
    ch = Serial.read();
    str += (char)ch;
    len++;
    delay(2);
  }
  if (len > 0)
  {
    Serial.println(str);

    //JsonCommands
    if (str.substring(0, 1) == "{")
    {
      String result = jsonParseAndProcess(str);
    }
    else
    {
    }
  }

}
