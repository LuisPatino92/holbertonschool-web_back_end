import { uploadPhoto, createUser } from './utils';

async function asyncUploadUser() {
  let photo = null;
  let user = null;

  try {
    photo = await uploadPhoto();
    user = await createUser();
  } finally {
    const uploadUser = {
      photo,
      user,
    };
  }

  return uploadUser;
}

export default asyncUploadUser;
