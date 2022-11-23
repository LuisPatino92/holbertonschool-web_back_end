function getListStudentIds(students) {
  if (Array.isArray(students)){
    const ids = students.map((item) => item.id);
    return ids;
  }
  return [];
}
export default getListStudentIds;
