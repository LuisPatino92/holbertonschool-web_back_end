import { uploadPhoto, createUser } from "./utils";

export function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((values) => {
      const { lastName } = values[1];
      const { firstName } = values[1];
      const { body } = values[0];
      console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch(() => console.log("Signup system offline"));
}
