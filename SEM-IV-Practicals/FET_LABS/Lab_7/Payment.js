export function paymentprocess(amount) {
  if (amount >= 1000) {
    alert(amount + " Payment Processed");
  } else {
    alert(amount + " Payment Failed");
  }
}
