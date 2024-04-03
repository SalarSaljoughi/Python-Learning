// from data.js
var tableData = data;


var tbody = d3.select("tbody");

console.log(data);


// search date
d3.select("#filter-btn").on("click", function () {
  tbody.selectAll("tr").remove()
  event.preventDefault()
  input = document.getElementById("datetime").value
  tableData = data.filter(function (d) {
    return d.datetime == input;
  })
  tableData.map(x => {
    let newTr = tbody.append('tr');
    Object.values(x).forEach(val => {
      newTr.append('td').text(val)
    })
  })
})



// Import data into HTML table
data.map(x => {
  let newTr = tbody.append('tr');
  Object.values(x).forEach(val => {
    newTr.append('td').text(val)
  })
})



// Function to search data with user input.
function search() {
  var input, filter, table, tr, td, i, j, tds, ths, matched;
  input = document.getElementById("searchInput");
  filter = input.value.toUpperCase();
  tr = document.getElementsByTagName("tr");

  // Loop through all table rows, and hide
  // those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    tds = tr[i].getElementsByTagName("td");
    ths = tr[i].getElementsByTagName("th");
    matched = false;

    // leave the row header 
    if (ths.length > 0) {
      matched = true;
    }
    else {
      for (j = 0; j < tds.length; j++) {
        td = tds[j];
        if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
          matched = true;
          break;
        }

      }
    }
    if (matched == true) {
      tr[i].style.display = "";
    }
    else {
      tr[i].style.display = "none";
    }
  }
}
