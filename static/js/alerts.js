(function($) {
  showSwal = function(type,form) {
    'use strict';
    // const fundTransferForm = document.getElementById('fund-transfer-form')
    if (type === 'basic') {
      swal({
        text: 'Any fool can use a computer',
        button: {
          text: "OK",
          value: true,
          visible: true,
          className: "btn btn-primary"
        }
      })

    } else if (type === 'title-and-text') {
      swal({
        title: 'Read the alert!',
        text: 'Click OK to close this alert',
        button: {
          text: "OK",
          value: true,
          visible: true,
          className: "btn btn-primary"
        }
      })

    } else if (type === 'success-message') {
      swal({
        title: 'Congratulations!',
        text: 'You entered the correct answer',
        icon: 'success',
        button: {
          text: "Continue",
          value: true,
          visible: true,
          className: "btn btn-primary"
        }
      })

    } else if (type === 'auto-close') {
      swal({
        title: 'Auto close alert!',
        text: 'I will close in 2 seconds.',
        timer: 2000,
        button: false
      }).then(
        function() {},
        // handling the promise rejection
        function(dismiss) {
          if (dismiss === 'timer') {
            console.log('I was closed by the timer')
          }
        }
      )
    } else if (type === 'warning-message-and-cancel') {
      swal({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true
          }
        }
      })

    } else if (type === 'custom-html') {
      swal({
        content: {
          element: "input",
          attributes: {
            placeholder: "Type your password",
            type: "password",
            class: 'form-control'
          },
        },
        button: {
          text: "OK",
          value: true,
          visible: true,
          className: "btn btn-primary"
        }
      })
    } else if (type === 'withdrawal-request') {
      if(form?.classList.contains('d-none'))
        form.classList.remove('d-none')
      swal({
        content: form,
        buttons: {
          submit: {
            text: "Submit",
            value: false,
            visible: true,
            className: "btn btn-success",
            loaderHtml: '',
            closeModal: false,
          },
          cancel: {
            text: "Cancel",
            value: true,
            visible: true,
            className: "btn btn-danger",
            closeModal: true  
          }
        }
      })
      document.getElementsByClassName('swal-button--submit')[0].addEventListener('click',()=>{
        // remove the unnecessary loader
        const loader = document.getElementsByClassName('swal-button__loader')[0]
        if(loader) loader.remove()
        // perform validations
        const amount = document.getElementById('amount-in-wdr')
        const countWarning = document.getElementById('amount-warning-in-wdr')
        if (countWarning.classList.contains('d-none') && amount.value !== '' ){
          form.submit()
        }
        else{
          const warning = document.getElementById('fix-errors')
          warning.classList.remove('d-none')
          console.log('problem')
        }
      })
  
    }
    else{
      console.log("Type not mentioned in alert.js")
    }
  }

})(jQuery);