const controlBox = document.getElementById("controls")
function handleClick(number) {
  const buttons = controlBox.children
  const cards = document.getElementsByClassName('table-cards')
  for (let i = 0; i < buttons.length; i++) {
    buttons[i].classList.remove('btn-primary')
    buttons[i].classList.remove('active')
    buttons[i].classList.add('btn-outline-primary')
    // buttons[i].classList.add('btn-fw')
    cards[i].classList.add('d-none')
  }

  buttons[number].classList.add('btn-primary')
  buttons[number].classList.add('active')
  buttons[number].classList.remove('btn-outline-primary')
  // buttons[number].classList.remove('btn-fw')
  cards[number].classList.remove('d-none')
  
}

for (let i = 0; i < controlBox.children.length; i++) {
  controlBox.children[i].addEventListener('click', () => handleClick(i))
}