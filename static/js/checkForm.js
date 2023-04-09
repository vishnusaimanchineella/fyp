
function validateForm() {
    var age = document.getElementById("age").value;
    var weight = document.getElementById("weightt").value;
    var height = document.getElementById("height").value;
    var agevalue = parseInt(age);
    var weightvalue = parseInt(weight);
    var heightvalue = parseInt(height);
    if (agevalue<5 || agevalue>90) {
        alert("Age must be between 5 and 90.");
      return false;
    }
  
    if (isNaN(age)) {
      alert("Age must be a number.");
      return false;
    }
   
    if (weightvalue<5 || weightvalue>150) {
        alert("Weight must be between 5kgs and 150kgs.");
        return false;
    }
  
    if (isNaN(weight)) {
      alert("Weight must be a number.");
      return false;
    }
  
    if (heightvalue<40 || heightvalue>240) {
        alert("Height must be between 40 cms and 240 cms.");
      alert("Please enter your height.");
      return false;
    }
  
    if (isNaN(height)) {
      alert("Height must be a number.");
      return false;
    }
  
    return true;
  }
  