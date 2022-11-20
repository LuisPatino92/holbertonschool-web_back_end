function uploadPhoto(filename) {
  const prom = Promise.reject(new Error(`${filename} cannot be processed`));

  return prom;
}

export default uploadPhoto;
