function getFormData(form) {
  let formData = {};
  for ( var i = 0; i < form.elements.length; i++ ) {
    var e = form.elements[i];
    console.log(e)
    if (e.type == 'checkbox') {
      formData[e.name] = {type: e.type, value: e.checked};
    } 
    else {
      formData[e.name] = {type: e.type, value: e.value};
    }
  }
  return formData;
}

function addRecord(formId, tableName) {
  var form = document.forms[formId];
  fetch(`/api/addTableRecord/${tableName}`, {
    method: 'POST',
    body: JSON.stringify(getFormData(form)),
    headers: {"Content-type": "application/json; charset=UTF-8"}
  }).then((response) => response.json())
    .then((json) => {
      handleFormApiResponse(json, form);
    })
} 

function addColumn(formId, tableName) {
    var form = document.forms[formId];
    fetch(`/api/addTableColumn/${tableName}`, {
      method: 'POST',
      body: JSON.stringify(getFormData(form)),
      headers: {"Content-type": "application/json; charset=UTF-8"}
    }).then((response) => response.json())
      .then((json) => {
        handleFormApiResponse(json, form);
      })
}

function editRecord(formId, tableName) {
  var form = document.forms[formId];
  fetch(`/api/editRecord/${tableName}`, {
    method: 'POST',
    body: JSON.stringify(getFormData(form)),
    headers: {"Content-type": "application/json; charset=UTF-8"}
  }).then((response) => response.json())
    .then((json) => {
      handleFormApiResponse(json, form);
    })
}

function handleFormApiResponse(data, form) {
  let s = data.status;
  if (s == 'OK') {
    form.reset();
    closeModal();
    // Todo: replace this with code that just updates the table
    location.replace(location.href);
  } else if (s == 'error') {
    alert(data.msg);
  }
}

function loadEditRecordModal(tableName, id) {
  let form = 'editRecordForm';
  fetch(`/api/getRecord/${tableName}/${id}`)
    .then((response) => response.json())
    .then((json) => {
      populateModalFields(form, json);
    })
}

function populateModalFields(formId, data) {
  let f = document.forms[formId];
  for ( var i = 0; i < f.elements.length; i++ ) {
    f.elements[i].setAttribute('value', data[f.elements[i].id]) ;
  }
}

function closeModal() {
  let m = document.getElementsByClassName('modal');
  for (var i = 0; i < m.length; i++) {
    var modal = bootstrap.Modal.getInstance(m.item(i))
    if (modal) modal.hide();
  }
}

function toDateInputValue(dateObject){
  const local = new Date(dateObject);
  local.setMinutes(dateObject.getMinutes() - dateObject.getTimezoneOffset());
  console.log( local.toJSON())
  return local.toJSON().slice(0,16);
};