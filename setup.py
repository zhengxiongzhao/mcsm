import setuptools
import versioneer

setuptools.setup(
    name="mcsm_template",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
