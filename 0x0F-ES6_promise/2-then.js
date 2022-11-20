function handleResponseFromAPI(promise) {
  const handled = promise
    .then(() => ({
      status: 200,
      body: "success",
    }))
    .catch(() => Error())
    .finally(() => console.log("Got a response from the API"));
  return handled;
}

export default handleResponseFromAPI;
