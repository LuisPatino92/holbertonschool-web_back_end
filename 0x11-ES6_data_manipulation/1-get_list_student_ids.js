function getListStudentIds(students) {
  const ids = students.map((item) => item.id);
  if (Array.isArray(students)){
    return ids;
  }
  return [];
}
export default getListStudentIds;
