import { validateinfo } from "./Validate.js";
import { paymentprocess } from "./Payment.js";
import { rating } from "./Rate.js";

function validation() {
  let name = prompt("Enter Your Name :");
  validateinfo(name);
  let amount = prompt("Enter Amount :");
  paymentprocess(amount);
  let rate = prompt("Enter Rating :");
  rating(rate);
}

validation();
