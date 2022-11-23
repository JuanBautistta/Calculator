// C++ code

#define NUMBER_OF_LEDS 4
#define ON 1
#define OFF 0
#define TRUE 1
#define FALSE 0

int leds[] = {13, 12, 11, 10};         // define the leds to use
char turn_on[] = {'1', '1', '1', '1'}; // define all the leds as on

// the setup function runs once when you press reset or power the board
void setup()
{
  //configure all the leds of the leds array as output.
  for(int i=0; i<NUMBER_OF_LEDS; i++){ 
    pinMode(leds[i], OUTPUT);
  }
  /*This tells the Arduino to get ready to exchange messages with the Serial 
  Monitor at a data rate of 9600 bits per second. That's 9600 binary ones or 
  zeros per second, and is commonly called a baud rate.*/
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop()
{
  /*Get the number of bytes (characters) available for reading from the serial 
  port. This is data that's already arrived and stored in the serial receive 
  buffer (which holds 64 bytes).*/
  if (Serial.available()){
    /*reads characters from the serial buffer into an array. The function 
    terminates if the terminator character is detected, the determined length 
    has been read, or it times out (see Serial.setTimeout()). In this case if 
    the \n caracter is detected, store the result in turn_on and only read 4
    digits*/
  	Serial.readBytesUntil('\n', turn_on, 4);
  }
  /*call the functions loop_led1, loop_led2, loop_led3 and loop_led4 with the 
  values of the array turn_on at position i with i=0,1,2,3*/
  loop_led1(turn_on[0]);
  loop_led2(turn_on[1]);
  loop_led3(turn_on[2]);
  loop_led4(turn_on[3]);
}

/*
turns led1 on or off according to the status received as a parameter
*/
void loop_led1(char state)
{
  if(state == '1'){            // check the decease state of the led
    digitalWrite(leds[0], ON); // turn on the led
    //allows you to pause the execution of your Arduino program for a specified period
    delay(1000);
  } else {
    digitalWrite(leds[0], OFF); // turn off de led
  }
}

/*
turns led2 on or off according to the status received as a parameter
*/
void loop_led2(char state)
{
  if(state == '1'){
    digitalWrite(leds[1], ON);
  } else {
    digitalWrite(leds[1], OFF);
  }
}

/*
turns led3 on or off according to the status received as a parameter
*/
void loop_led3(char state)
{
  if(state == '1'){
    digitalWrite(leds[2], ON);
  } else {
    digitalWrite(leds[2], OFF);
  }
}

/*
turns led4 on or off according to the status received as a parameter
*/
void loop_led4(char state)
{
  if(state == '1'){
    digitalWrite(leds[3], ON);
  } else {
    digitalWrite(leds[3], OFF);
  }
}