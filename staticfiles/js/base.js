window,addEventListener('DOMContentLoaded', () => {

  /*
   * Add Animation to the burger Menu 
  */
  const burgerToggler = document.getElementsByClassName('navbar-toggler')[0];
  let isOpen = false;
  burgerToggler.addEventListener('click', () => {
    console.log(isOpen)
    if (!isOpen) {
      burgerToggler.classList.add('open');
      isOpen = true;
    }
    else {
      burgerToggler.classList.remove('open');
      isOpen = false;
    }
  })

  /*
   * Remove the message after 3 seconds
  */
  const messageContainer = document.getElementsByClassName('message-container')[0];
  if(messageContainer){
    setTimeout(() => {
      messageContainer.remove()
    }, 4000)
  }

})