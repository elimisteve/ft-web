(function() {
  // Append '?js-enabled' to each form's action (URL)
  var forms = document.getElementsByTagName('form');
  for (var i = 0; i < forms.length; i++) {
    forms[i].action += '?js-enabled';
  }
})()
