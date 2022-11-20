function signUpUser(firstName, lastName) {
  const prom = Promise.resolve({
    firstName,
    lastName,
  });

  return prom;
}

export default signUpUser;
