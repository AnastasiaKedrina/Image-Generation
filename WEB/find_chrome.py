import undetected_chromedriver as uc

# Создайте экземпляр ChromeDriver
driver = uc.Chrome()

# Получите путь к используемому ChromeDriver
driver_path = driver.service.path
print(f"Путь к ChromeDriver: {driver_path}")

# Не забудьте закрыть драйвер
driver.quit()
