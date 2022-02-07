// Some javascript code to use


import { askDelete } from "./utils.js";

/**
 * 
 * @returns The html elements of the delete buttons
 */
const getButtonsDelete = () => {
  const deleteButton = document.querySelectorAll('.delete-button');
  return deleteButton;
}


// getting the button
const buttonsList = getButtonsDelete();

buttonsList.forEach((button) => {
  button.addEventListener('click', (e) => {
    const result = askDelete('You want delete this product?');
    if (!result) {
      e.preventDefault();
    }
  });
});