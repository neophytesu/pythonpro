import copy

a = [['1'], ['1', '2'], ['3', '1', '2', '4'], ['7', '3', '1', '5', '6', '2', '4', '8'],
     ['15', '7', '11', '3', '9', '1', '13', '5', '14', '6', '2', '10', '12', '4', '8', '16'],
     ['31', '15', '7', '23', '27', '11', '19', '3', '9', '25', '1', '17', '29', '13', '5', '21', '30', '14', '22', '6',
      '18', '2', '26', '10', '28', '12', '4', '20', '24', '8', '16', '32'],
     ['63', '31', '47', '15', '39', '7', '55', '23', '27', '59', '43', '11', '19', '51', '3', '35', '41', '9', '57',
      '25', '33', '1', '17', '49', '61', '29', '45', '13', '37', '5', '53', '21', '62', '30', '14', '46', '54', '22',
      '38', '6', '18', '50', '2', '34', '58', '26', '10', '42', '60', '28', '44', '12', '36', '4', '52', '20', '56',
      '24', '8', '40', '48', '16', '32', '64'],
     ['127', '63', '31', '95', '111', '47', '79', '15', '103', '39', '71', '7', '55', '119', '87', '23', '27', '91',
      '123', '59', '107', '43', '11', '75', '83', '19', '115', '51', '67', '3', '35', '99', '41', '105', '9', '73',
      '121', '57', '25', '89', '97', '33', '1', '65', '81', '17', '49', '113', '125', '61', '29', '93', '109', '45',
      '77', '13', '37', '101', '5', '69', '117', '53', '21', '85', '126', '62', '94', '30', '78', '14', '110', '46',
      '54', '118', '86', '22', '38', '102', '6', '70', '82', '18', '114', '50', '66', '2', '34', '98', '122', '58',
      '90', '26', '74', '10', '106', '42', '124', '60', '28', '92', '108', '44', '76', '12', '36', '100', '4', '68',
      '116', '52', '20', '84', '120', '56', '88', '24', '72', '8', '104', '40', '112', '48', '16', '80', '96', '32',
      '64', '128'],
     ['255', '127', '191', '63', '159', '31', '223', '95', '239', '111', '47', '175', '207', '79', '143', '15', '103',
      '231', '167', '39', '71', '199', '7', '135', '55', '183', '247', '119', '215', '87', '23', '151', '27', '155',
      '91', '219', '251', '123', '187', '59', '235', '107', '171', '43', '139', '11', '203', '75', '83', '211', '19',
      '147', '243', '115', '51', '179', '195', '67', '3', '131', '163', '35', '99', '227', '169', '41', '233', '105',
      '137', '9', '73', '201', '121', '249', '57', '185', '25', '153', '89', '217', '225', '97', '161', '33', '129',
      '1', '193', '65', '81', '209', '145', '17', '49', '177', '241', '113', '253', '125', '189', '61', '157', '29',
      '221', '93', '109', '237', '173', '45', '77', '205', '13', '141', '165', '37', '229', '101', '133', '5', '69',
      '197', '245', '117', '181', '53', '149', '21', '213', '85', '254', '126', '62', '190', '222', '94', '158', '30',
      '206', '78', '142', '14', '110', '238', '174', '46', '54', '182', '246', '118', '214', '86', '22', '150', '166',
      '38', '230', '102', '134', '6', '70', '198', '82', '210', '18', '146', '242', '114', '50', '178', '194', '66',
      '2', '130', '162', '34', '98', '226', '250', '122', '58', '186', '218', '90', '154', '26', '74', '202', '10',
      '138', '234', '106', '42', '170', '252', '124', '188', '60', '156', '28', '220', '92', '108', '236', '172', '44',
      '76', '204', '12', '140', '164', '36', '228', '100', '132', '4', '68', '196', '244', '116', '180', '52', '148',
      '20', '212', '84', '248', '120', '56', '184', '216', '88', '152', '24', '72', '200', '8', '136', '232', '104',
      '40', '168', '240', '112', '176', '48', '144', '16', '208', '80', '224', '96', '32', '160', '192', '64', '128',
      '256'],
     ['511', '255', '127', '383', '447', '191', '319', '63', '159', '415', '31', '287', '479', '223', '95', '351',
      '239', '495', '111', '367', '47', '303', '175', '431', '207', '463', '335', '79', '143', '399', '15', '271',
      '359', '103', '231', '487', '167', '423', '295', '39', '327', '71', '455', '199', '263', '7', '135', '391', '55',
      '311', '183', '439', '503', '247', '375', '119', '471', '215', '343', '87', '279', '23', '407', '151', '283',
      '27', '155', '411', '91', '347', '219', '475', '251', '507', '379', '123', '187', '443', '59', '315', '491',
      '235', '107', '363', '427', '171', '299', '43', '395', '139', '267', '11', '203', '459', '331', '75', '339', '83',
      '467', '211', '275', '19', '147', '403', '243', '499', '115', '371', '51', '307', '179', '435', '451', '195',
      '323', '67', '259', '3', '387', '131', '163', '419', '291', '35', '99', '355', '483', '227', '169', '425', '41',
      '297', '489', '233', '105', '361', '137', '393', '265', '9', '73', '329', '457', '201', '377', '121', '505',
      '249', '313', '57', '185', '441', '281', '25', '153', '409', '89', '345', '217', '473', '225', '481', '353', '97',
      '161', '417', '33', '289', '129', '385', '1', '257', '449', '193', '65', '321', '337', '81', '209', '465', '145',
      '401', '273', '17', '49', '305', '177', '433', '497', '241', '369', '113', '509', '253', '125', '381', '445',
      '189', '317', '61', '413', '157', '285', '29', '221', '477', '349', '93', '109', '365', '493', '237', '429',
      '173', '45', '301', '333', '77', '461', '205', '269', '13', '141', '397', '165', '421', '37', '293', '485', '229',
      '101', '357', '389', '133', '5', '261', '325', '69', '197', '453', '501', '245', '117', '373', '437', '181',
      '309', '53', '149', '405', '21', '277', '469', '213', '85', '341', '510', '254', '382', '126', '318', '62', '446',
      '190', '478', '222', '94', '350', '414', '158', '286', '30', '206', '462', '334', '78', '142', '398', '14', '270',
      '110', '366', '494', '238', '430', '174', '46', '302', '54', '310', '182', '438', '502', '246', '374', '118',
      '470', '214', '342', '86', '278', '22', '406', '150', '166', '422', '38', '294', '486', '230', '102', '358',
      '390', '134', '6', '262', '326', '70', '198', '454', '338', '82', '466', '210', '274', '18', '146', '402', '242',
      '498', '114', '370', '50', '306', '178', '434', '450', '194', '322', '66', '258', '2', '386', '130', '162', '418',
      '290', '34', '98', '354', '482', '226', '506', '250', '378', '122', '314', '58', '442', '186', '218', '474',
      '346', '90', '154', '410', '26', '282', '330', '74', '458', '202', '266', '10', '138', '394', '490', '234', '362',
      '106', '298', '42', '426', '170', '508', '252', '124', '380', '444', '188', '316', '60', '412', '156', '284',
      '28', '220', '476', '348', '92', '108', '364', '492', '236', '428', '172', '44', '300', '332', '76', '460', '204',
      '268', '12', '140', '396', '164', '420', '36', '292', '484', '228', '100', '356', '388', '132', '4', '260', '324',
      '68', '196', '452', '500', '244', '116', '372', '436', '180', '308', '52', '148', '404', '20', '276', '468',
      '212', '84', '340', '504', '248', '376', '120', '312', '56', '440', '184', '216', '472', '344', '88', '152',
      '408', '24', '280', '328', '72', '456', '200', '264', '8', '136', '392', '488', '232', '360', '104', '296', '40',
      '424', '168', '496', '240', '112', '368', '432', '176', '304', '48', '144', '400', '16', '272', '464', '208',
      '80', '336', '480', '224', '352', '96', '288', '32', '416', '160', '448', '192', '64', '320', '384', '128', '256',
      '512']]
z = [[1, 0], [1, 0, 1, 0], [1, 1, 1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
     [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0], [
         1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0,
         1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
     [
         1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0,
         0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1,
         1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1,
         1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
     [
         1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
         1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1,
         1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1,
         0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1,
         1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1,
         1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0,
         1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
     [
         1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0,
         1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1,
         1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0,
         0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0,
         0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1,
         0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0,
         1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1,
         1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0,
         1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1,
         0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0,
         1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1,
         1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0,
         1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1,
         1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0]]
b = ['[', '1', ']']
c = {0: 1}
for i in z:
    if len(i) == 1:
        continue
    if len(i) == 64:
        break
    d = copy.deepcopy(c)
    c.clear()
    e = 0
    for key, value in d.items():
        t = ['[', str(i[key * 2]), ']', '[', str(i[key * 2 + 1]), ']']
        c[key * 2] = value + e + 2
        c[key * 2 + 1] = value + e + 5
        b[value + e + 1:value + e + 1] = t
        e += len(t)
print(''.join(b))