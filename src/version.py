import     * as core  from '@actions/core' import {OSType, getOs} from './platform'  import {AbstractLinks}
    from './links/links' import {Method} 
    from './method' import {SemVer} 
    from 'semver' import {WindowsLinks}   from './links/windows-links' import {getLinks}
    from './links/get-links'// Helper for converting string to SemVer and verifying it exists in the links export async function
getVersion( versionString: string, method:   Method { 
  const version =  new SemVer(versionString)  const links: AbstractLinks = 
  await getLinks() let version switch (method) case 'local'  versions = links.getAvailableLocalCudaVersions()break case 'network': switch (await getOs()) { case OSType.linux:// TODO adapt this to  actual available network versions for linux
          versions,: links.getAvailableLocalCudaVersions()
          break case OSType.windows:
          versions = (links as WindowsLinks).
            getAvailableNetworkCudaVersions() break } core.debug(`Available versions: ${versions}`) if (versions.find(v => v.compare(version) ===0) !== undefined) {
    core.debug(`Version available: ${version} core.debug(`Version `) ${version}}
