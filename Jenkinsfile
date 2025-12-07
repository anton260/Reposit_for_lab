pipeline {
    agent any

    stages {
        stage('Build Package') {
            steps {
                sh 'mkdir -p build/DEBIAN build/usr/local/bin'
                sh 'cp count_files.sh build/usr/local/bin/'
                sh 'chmod +x build/usr/local/bin/count_files.sh'
                
                sh 'echo "Package: count-files" > build/DEBIAN/control'
                sh 'echo "Version: 1.0-1" >> build/DEBIAN/control'
                sh 'echo "Architecture: all" >> build/DEBIAN/control'
                sh 'echo "Maintainer: Student" >> build/DEBIAN/control'
                sh 'echo "Description: Lab 2 script" >> build/DEBIAN/control'
                
                sh 'dpkg-deb --build build count-files.deb'
            }
        }

        stage('Test in Docker') {
            steps {
                echo "--- Building Test Image ---"
                sh 'echo "FROM ubuntu:22.04" > Dockerfile.test'
                sh 'echo "COPY count-files.deb /tmp/packet.deb" >> Dockerfile.test'
                sh 'echo "RUN apt-get update && apt-get install -y /tmp/packet.deb" >> Dockerfile.test'
                sh 'echo "CMD /usr/local/bin/count_files.sh" >> Dockerfile.test'
                
                sh 'docker build -f Dockerfile.test -t test-image .'
                sh 'docker run --rm test-image'
            }
        }
    }
}
