// define global variables
var editMode     = false; // Change this base after implementing the checkbox
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
    if (editMode) {

        // check if the event target is not the editing cell
        if (editingCell != null && event.target.tagName != 'INPUT') {
            saveCellChanges(initValues)

        } else if (editingCell == null) {
            var srcElement = event.target || event.srcElement;
            if (srcElement.tagName == 'TD') {
                // if primaryKey not in the class list of the header cell then edit the cell
                if (!srcElement.classList.contains('primaryKey')) {
                    editCell(event);
                }
            }
        }
    }
});

function editCell(event) {
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
    inputField.focus();

    } 
}

function saveCellChanges(_callback) {
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
    // Do nothing if no changes were made
    if (inputField != null && inputField.value == oldValue) {
        editingCell.querySelector('input');
        editingCell.innerText = inputField.value;
        editingRow.classList.add('overflow-hidden'); 
        _callback();
        return   
    }
    // save the changes to the database
    // call the api at /api/editDb with the primary key values and the new value of the cell
    fetch('/api/updateDb', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            primaryKeys: primaryKeys,
            "table": editingRow.parentElement.parentElement.id,
            column: headerId,
            value: inputField.value
        })
    }).then(response => {
        if (!response.ok) {
            alert("Error saving changes to the database. Returning new value " + editingCell.innerText + " to previous value " + oldValue);
            editingCell.innerText = oldValue;
    }
    _callback();
})
}   

function initValues  () {
    editingCell  = null;
    editingRow   = null;
    editRowIndex = null;
    editColIndex = null;
    headerId     = null;   
    inputField   = null;
}