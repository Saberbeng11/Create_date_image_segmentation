import os
import cv2
def main():
    def extract_polygons(mask):
        """
        Trích xuất đa giác từ mask (ảnh nhị phân).

        Parameters:
            mask (numpy.ndarray): Ảnh nhị phân chứa đối tượng cần trích xuất.

        Returns:
            list: Danh sách các đa giác tương ứng với các đường viền của mask.
        """
        H, W = mask.shape  # Chiều cao và chiều rộng của mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Tìm các đường viền
        polygons_ls = []  # Danh sách chứa các đa giác
        for cnt in contours:
            if cv2.contourArea(cnt) > 200:  # Lọc ra các contour có diện tích lớn hơn 200
                polygon = []  # Danh sách tọa độ của đa giác
                for point in cnt:
                    x, y = point[0]
                    polygon.append(x / W)  # Chuẩn hóa tọa độ x để nằm trong khoảng [0, 1]
                    polygon.append(y / H)  # Chuẩn hóa tọa độ y để nằm trong khoảng [0, 1]
                polygons_ls.append(polygon)  # Thêm đa giác vào danh sách
        return polygons_ls

    input_dir = 'masks'  # Thư mục chứa các ảnh nhị phân (mask)
    output_dir = 'labels'  # Thư mục đầu ra chứa các file văn bản (labels)

    # Duyệt qua tất cả các tệp trong thư mục masks
    for j in os.listdir(input_dir):
        image_path = os.path.join(input_dir, j)  # Đường dẫn đầy đủ đến tệp ảnh
        mask = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Đọc ảnh nhị phân
        mask0 = cv2.threshold(mask, 130, 255, cv2.THRESH_BINARY)[1]  # Lọc màu xanh
        
        mask1 = cv2.threshold((mask == 113).astype('uint8') * 255, 230, 255, cv2.THRESH_BINARY)[1]  # Lọc màu đỏ
        
        # Trích xuất đa giác từ mask0 và mask1
        polygons_ls0 = extract_polygons(mask0)
        polygons_ls1 = extract_polygons(mask1)

        # Ghi thông tin của các đa giác vào các file văn bản
        with open('{}.txt'.format(os.path.join(output_dir, j)[:-4]), 'w') as f:
            for label, polygons_ls in enumerate([polygons_ls0, polygons_ls1]):  # Lặp qua mask0 và mask1
                for polygon in polygons_ls:  # Lặp qua danh sách đa giác
                    f.write('{} '.format(label))  # Ghi nhãn (0 cho mask0, 1 cho mask1)
                    for p_ in polygon:
                        f.write('{} '.format(p_))  # Ghi tọa độ của các đỉnh của đa giác
                    f.write('\n')  # Xuống dòng cho đa giác tiếp theo
    
        # Đóng file văn bản
        f.close()
        
        # Hiển thị ảnh quá trình làm việc 
        print("đã ghi")
        all_color_class = cv2.imread("masks\\all_0.png",1) 
        origin_image = cv2.imread("original image//all_0.jpg",1) 
        # cv2.imshow("Color_class",all_color_class)
        # cv2.imshow("Origin image",origin_image)
        # cv2.imshow("Gray class",mask)
        # cv2.imshow("Green class",mask0)
        # cv2.imshow("Red class",mask1)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

if __name__ == "__main__":
    main()