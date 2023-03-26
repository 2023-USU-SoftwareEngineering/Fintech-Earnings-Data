<template>
    <div class="pricetrend" id="pricetrend">
      <header>
      </header>
      <section>
      </section>
  <form action="/action_page.php">
  <label for="prediction">Select a time period: </label>
  <select id="time" name="time">
    <option value="short">Short</option>
    <option value="medium">Medium</option>
    <option value="long">Long</option>
  </select>
  <select id="companies" name="companies">
  </select>
  </form>
  <button @click="getPrediction()">Get Prediction</button>
    </div>
    
  </template>

  <script>
  // This export and populate function will run whenever you open the pricetrend page
    export default {
      mounted() {
        this.myMethod();
      },
      methods: {
      myMethod() {
        //console.log('This runs every time you open the page');
        async function populate() {
          //Gather the list of companies and store them into the variable "companies"
          const requestURL = 'http://localhost:8000/companies/list'; //change to mater
          const request = new Request(requestURL);

          const response = await fetch(request);
          const companies = await response.json();
          
          // Test to make sure the list got pulled
          //console.log(companies.info[1][0]);

          // Create and then select the drop down element for the companies in the form
          var companydropdown = document.getElementById("companies");

          // Condition to make sure it does not load the company list into the drop down more than once, by checking to see if the first company listed is already an option
          var elementExists = document.getElementById(companies.info[0]);
          if (!(elementExists)) {
            //console.log('Populating the company list drop down');
            // Populates the drop down box with companies from our server
            for (var i=0; i < companies.info.length; i++) {
            var companyoption = document.createElement("option");
            companyoption.setAttribute("value", companies.info[i]);
            companyoption.setAttribute("id", companies.info[i]);
            companyoption.textContent = companies.info[i][0];
            companydropdown.appendChild(companyoption);
            }
          }
        }
        populate();
        return 'hello world!';
      },
      async getPrediction() {
        // Saves the selected values from the form
        var timevalue = document.getElementById("time").value;
        var companyvalue = document.getElementById("companies").value;

        // Test to make sure it pulled the selected values
        //console.log(timevalue);
        //console.log(companyvalue);

        const requestURLresult = 'http://localhost:8000/prediction/pull?company='+companyvalue+'&type='+timevalue; //change to mater
        const requestresult = new Request(requestURLresult);

        const responseresult = await fetch(requestresult);
        const companiesresult = await responseresult.json();
        console.log(companiesresult.prediction.info); // update once prediction data is formatted

        // Create the result element and add it to the document
        // First get the element of the page itself
        var mainpage = document.getElementById("pricetrend");

        // Then check for the previous prediction (if any) and remove it
        var predictionExists = document.getElementById("finalresult");
        if ((predictionExists)) {
          predictionExists.remove();
          console.log('Deleted Old Prediction')
        }
        // Then create a div for the result and append it
        var resultelement = document.createElement("div");
        resultelement.setAttribute("id", "finalresult");
        resultelement.textContent = "Prediction goes here"; //Change this to print the prediction value, maybe set up a dummy value to test?
        mainpage.appendChild(resultelement);
        console.log('New Prediction made!')

        return 'hello world!';
      }
    },
    }
  </script>