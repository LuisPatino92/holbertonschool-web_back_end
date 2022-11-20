export default function loadBalancer(chinaDownload, USDownload) {
  const prom = Promise.race([chinaDownload, USDownload]);
  return prom;
}
