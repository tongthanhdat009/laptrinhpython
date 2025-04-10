class XuatXu:
    def __init__(self, ma_xuat_xu, ten_xuat_xu):
        self.__ma_xuat_xu = ma_xuat_xu
        self.__ten_xuat_xu = ten_xuat_xu
        
    @property
    def ten_xuat_xu(self):
        return self.__ten_xuat_xu
    def ten_xuat_xu(self, value):
        self.__ten_xuat_xu = value
        
    @property
    def ma_xuat_xu(self):
        return self.__ma_xuat_xu
    def ma_xuat_xu(self, value):
        self.__ma_xuat_xu = value