function searchTable() {
    var input=document.getElementById("searchInput").value.toLowerCase();
    console.log(input)
    var table =document.getElementById("dataTable");
    var rows =table.getElementsByTagName("tr");
    
    
    
    // Loop through all table rows
    for(var i=1; i< rows.length; i++){
        var cells=rows[i].getElementsByTagName("td");
        var match=false;
        

        // Loop through each cell to check if it contains
        for (var j=0; j < cells.length; j++) {
          if (cells[j]) {
            var cellText = cells[j].innerText.toLowerCase();
            if (cellText==input) {
                match =true;
                break;
            }
          }
        }

        rows[i].style.display = match ? "" :"none";
    }
}


function printReport() {
    var printContent = document.getElementById('dataTable').outerHTML;
    var originalContent = document.body.innerHTML;

    document.body.innerHTML = printContent;
    window.print();
    document.body.innerHTML = originalContent;
}

 




