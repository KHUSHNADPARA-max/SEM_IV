export function validateinfo(name) {
  if (typeof name === typeof 'string'  ) {
    alert("Name Varified : " + name);
  } else {
    alert("Name Not Varified : " + name);
  }
}
