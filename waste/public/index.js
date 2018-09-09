   // Initialize Firebase
  var config = {
    apiKey: "AIzaSyDPrPYAQr3ZpvRSD4v3ZaGNgLfA00pyzZE",
    authDomain: "fir-iot-616d2.firebaseapp.com",
    databaseURL: "https://fir-iot-616d2.firebaseio.com",
    projectId: "fir-iot-616d2",
    storageBucket: "fir-iot-616d2.appspot.com",
    messagingSenderId: "666234619038"
  };
  firebase.initializeApp(config);

  var count=0;
  var sensorData = firebase.database().ref('dataValue');
  var retrieveData = firebase.database().ref('dataValue');
// listen submit form
 document.getElementById('submit').addEventListener('click',submitForm);

 function submitForm(e) {
 	e.preventDefault();
 	var name = getInputValue('name');
 	var mobileNumber = getInputValue('mobile');
  var user = document.getElementById("details");
 	// save data
   saveData(name,mobileNumber);
   count=count+1;
   // retrieve Data
   retrieveData.on('value',gotData);
  console.log(count);
 	console.log(name);
 	console.log(mobileNumber);
  var division = document.getElementById('details');
    division.innerHTML = name ;
 }
 function getInputValue(id) {
 	return document.getElementById(id).value;
 }
function saveData(name,mobileNumber){
    sensorData.child("Data "+count).set({
 		name:name,
 		mobileNumber:mobileNumber
   	});
}
function gotData(data){
  console.log(data.val());
  var gettedData = data.val();
  var keys = Object.keys(gettedData);
  for(var i=0;i< keys.length;i++){
    var k = keys[i];
    var gettedName = gettedData[k].name;
    var gettedMobNumber = gettedData[k].mobileNumber;
    // console.log(gettedName,gettedMobNumber);
  }
}