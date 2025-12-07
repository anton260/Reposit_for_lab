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
            agent { 
                docker { image 'ubuntu:22.04' } 
            }
            steps {
                sh 'apt-get update'
                sh 'apt-get install -y ./count-files.deb'
                
                echo "--- Executing the script ---"
                sh '/usr/local/bin/count_files.sh'
            }
        }
    }
}
