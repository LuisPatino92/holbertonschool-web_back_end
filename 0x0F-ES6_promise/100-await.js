import { uploadPhoto, createUser } from './utils';

async function asyncUploadUser() {
  const uploadUser = {
    photo: null,
    user: null
  }

  try {
    uploadUser.photo = await uploadPhoto();
    uploadUser.user = await createUser();
  } finally { }

  return uploadUser;
}

export default asyncUploadUser;
