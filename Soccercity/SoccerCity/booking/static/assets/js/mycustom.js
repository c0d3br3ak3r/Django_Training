function checkSlots(submit_url) {
  var form = $('#slots');
  var result_flag = false;
  $.ajax({
    async : false, //wait for form response before returning the function return value.
    url: submit_url,
    type : form.attr('method'),
    data : form.serialize(),
    success : function(response) {
      if(response.errors) {
        alert(response.errors);
      } else {
        result_flag = true;
      }
    },
    failure : function(data) {
      alert("Not able to contact server. Please try again later.")
    }
  });

  return result_flag;
}
