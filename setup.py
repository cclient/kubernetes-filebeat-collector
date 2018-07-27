from setuptools import setup
import filebeat


setup(name='k8s-filebeat-collector',
      version=filebeat.__version__,
      description=filebeat.__description__,
      author=filebeat.__author__,
      url='https://github.com/cclient/kubernetes-filebeat-collector',
      license=filebeat.__license__,
      platforms=['all'],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: collector kubernetes docker contain json-file and mount path files by filebeat',
      ],
      py_modules=['k8s-filebeat-collector'],
      )
