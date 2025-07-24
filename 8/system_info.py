import os
import sys

cwd = os.getcwd()
print("현재 작업 디렉토리:", cwd)

print("Python 버전:", sys.version)
print("운영체제:", os.name)

path_env = os.environ.get('PATH', '')
print("환경 변수 PATH 일부:", ':'.join(path_env.split(':')[:4]))

sample_path = "/Users/username/documents/report.txt"
directory, filename = os.path.split(sample_path)
name, ext = os.path.splitext(filename)

print("파일 경로 정보:")
print("- 디렉토리:", directory)
print("- 파일명:", filename)
print("- 확장자:", ext)

file_exists = os.path.exists(sample_path)
print("파일 존재 여부:", file_exists)
