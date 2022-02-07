/**
 * Some utils functions to use
 */

/**
 * 
 * @param {strgin} askText The text for show in the ask
 * @returns The result boolean value
 */
export function askDelete(askText) {
  const result = confirm(askText);
  return result;

}