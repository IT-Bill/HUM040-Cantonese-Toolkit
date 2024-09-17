import base64, json
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import (
    TencentCloudSDKException,
)
from tencentcloud.asr.v20190614 import asr_client, models


def sentence_recognition(file):
    # 初始化凭证
    cred = credential.Credential(
        # remove ID
    )
    audio_data = file.read()
    req = models.SentenceRecognitionRequest()
    req.EngSerViceType = "16k_yue"
    req.SourceType = 1
    req.VoiceFormat = "mp3"
    req.Data = base64.b64encode(audio_data).decode()
    
    client = asr_client.AsrClient(cred, "ap-guangzhou")
    return json.loads(client.SentenceRecognition(req).to_json_string())
