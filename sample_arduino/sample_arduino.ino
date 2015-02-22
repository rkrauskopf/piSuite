#define numberOfBytes 5
boolean isConnected = false;

void setup(){
  Serial.begin(9600);
  
  //Make sure that the arduino is connect to a valid usb port that
  //is receiving our data
  //establishContact();
}

#define numberOfBytes 4
void loop(){
  /*
    Arduino has trouble concatenating string of different value types
      (Ex.) String x = int + string 
      gives unexpected results so an int input value needs to be cast a string before
      being concatenated into the serial string being sent over the wire.
  */
  String inputA = String(random(0, 10));
  String inputB = String(random(20,200));
  String inputC = String(random(0, 100));
  String degree = String(random(0,100));  
  
  String serialString = "{\"input 1\" :" + inputA + ",";
  serialString += " \"input 2\" : " + inputB + ",";
  serialString += " \"Degrees\" : " + degree + ",";
  serialString += "\"input 3\" : " + inputC + "}";
    
  Serial.println(serialString);
  //30 second cycle if a connection is detected.
  delay(10000);
}
