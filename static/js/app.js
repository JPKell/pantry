// define global variables
var editMode     = true; // Change this base after implementing the checkbox
var editingCell  = null;
var editingRow   = null;
var editRowIndex = null;
var editColIndex = null;
var headerId     = null;   
var inputField   = null;
var oldValue     = null;

function toggleEditMode(checkbox) { editMode = !(checkbox == undefined); };

// create a listener for all mouse clicks and if there is an element being edited then save the changes
document.addEventListener('click', function(event) {
    console.log("Click EVENT ATART")
    if (editMode) {
        console.log("Edit mode active")

        // check if the event target is not the editing cell
        if (editingCell != null && !editingCell.contains(event.target)) {
            // check that event target does not contain the editingCell
            console.log("Save cell")

            saveCellChanges();
            editingCell = null;
            editingRow  = null;
        } else if (editingCell == null) {
            console.log("Try to edit")

            var srcElement = event.target || event.srcElement;
            if (srcElement.tagName == 'TD') {
                console.log("Edit cell")
                
                editCell(event);
            }
        }   else {
            console.log("Do nothing", editingCell)
        }
    }
});

function editCell(event) {
    console.log("Run editCell")
    
    if (editMode) {
      // Gather information about the cell being edited
      editingCell = event.target || event.srcElement;
      editColIndex = editingCell.cellIndex;
      editRowIndex = editingCell.parentElement.rowIndex;

      editingRow = editingCell.parentElement;
      // fint the column index of the cell being edited then get the id of the element at that index in the header row
      var headerRow = editingRow.parentElement.parentElement.querySelector('thead tr');
      var headerCell = headerRow.children[editingCell.cellIndex];
      headerId = headerCell.id;

      // create the input field for the editingCell
      inputField = document.createElement('input');
      inputField.type = 'text';
      oldValue = editingCell.innerText;
      inputField.value = oldValue;
      inputField.size = inputField.value.length;
      inputField.onblur = function() {
        editingCell.innerText = inputField.value;
      };

      // get the parent row and for the editingCell  
      editingRow.classList.remove('overflow-hidden');

      editingCell.innerText = '';
      editingCell.appendChild(inputField);
    } 
}

function saveCellChanges() {
    console.log("Run saveCellChanges")
    // get the current value of the input field
    // find all elements in the header row that have primaryKey in their class list
    var headerRow = editingRow.parentElement.parentElement.querySelector('thead tr');
    // create object to store the primary key values
    var primaryKeys = {};
    for (var i = 0; i < headerRow.children.length; i++) {
        if (headerRow.children[i].classList.contains('primaryKey')) {
            primaryKeys[headerRow.children[i].id] = editingRow.children[i].innerText;
        }
    }

    // get the value of the input field in the editing cell or iff the editing cell is an input get it from there
    // if (editingCell.querySelector('input') != null ) {
    //     input = editingCell.querySelector('input');
    // } else if ( editingCell.type == 'input' ) {
    //     input = editingCell;
    // } 
  // Do nothing if no changes were made

    if (inputField != null && inputField.value == oldValue) {
        editingCell.querySelector('input');
        editingCell.innerText = inputField.value;
        editingRow.classList.add('overflow-hidden');    
    }

    // save the changes to the database
    // call the api at /api/editDb with the primary key values and the new value of the cell
    console.log("Fetching")
    fetch('/api/editDb', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            primaryKeys: primaryKeys,
            column: headerId,
            value: inputField.value
        })
    }).then(response => {
        if (!response.ok) {
            console.log("Error", editingCell)
            if (editingCell != null && editingCell.type == 'input') {
            editingCell.value = oldValue;
        }   
    }
})
}   
