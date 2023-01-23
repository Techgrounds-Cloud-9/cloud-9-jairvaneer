# Amazon Certificate Manager
import boto3
import certmaker
from os.path import exists

def generate_certificate():
    if exists('arn.txt'):
        f = open('arn.txt','r+')
        return f.read()
    else:
        acm = boto3.client('acm')
        response=acm.import_certificate(
            Certificate=certmaker.certificate_pem,
            PrivateKey=certmaker.private_key_pem,
            CertificateChain=certmaker.ca_certificate_pem,
            )
        arn = response['CertificateArn'] 
        f = open('arn.txt','w+')
        f.write(arn)
        return arn
generate_certificate()

