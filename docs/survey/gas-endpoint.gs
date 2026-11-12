/**
 * Google Apps Script Endpoint untuk Survei Otomotif Visual 3D
 * Deploy sebagai Web App: Execute as Me, Who has access: Anyone
 *
 * Setup:
 * 1. Buat Google Sheet baru untuk simpan respons
 * 2. Copy Spreadsheet ID dari URL: https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit
 * 3. Ganti SPREADSHEET_ID di bawah
 * 4. Deploy → New deployment → Web app → Anyone
 * 5. Copy URL → paste ke index.html FORM_ENDPOINT
 */

// Terima ID polos ATAU URL spreadsheet lengkap (paste dari address bar).
// openById() menolak URL — selalu ekstrak 25+ char ID-nya.
const SPREADSHEET_REF = 'YOUR_SPREADSHEET_ID_HERE'; // GANTI INI
const SPREADSHEET_ID = (String(SPREADSHEET_REF).match(/[-\w]{25,}/) || [''])[0];
const SHEET_NAME = 'Responses';

function jsonOut(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function doPost(e) {
  // e kosong = fungsi dijalankan manual dari editor (Run), bukan lewat HTTP.
  // Tanpa guard ini yang muncul cuma TypeError 'reading postData' yang tidak
  // memberi tahu apa pun. Untuk uji manual pakai testSubmit().
  if (!e || !e.postData || !e.postData.contents) {
    console.error('doPost dipanggil tanpa event HTTP (Run manual?). Pakai testSubmit() untuk uji manual.');
    return jsonOut({
      success: false,
      error: 'No HTTP event. doPost harus dipanggil via POST, bukan Run manual di editor.'
    });
  }

  try {
    const data = JSON.parse(e.postData.contents);

    // Validasi basic
    if (!data || !data.q_contact_email) {
      return jsonOut({ success: false, error: 'Missing required fields' });
    }

    const sheet = getOrCreateSheet();
    appendRow(sheet, data);

    return jsonOut({ success: true });

  } catch (err) {
    console.error('Survey submit error:', err);
    return jsonOut({ success: false, error: err.toString() });
  }
}

function doGet(e) {
  // Health check saja. ContentService TIDAK bisa mengirim header CORS, dan Apps
  // Script tidak menjawab preflight OPTIONS — itu sebabnya klien memakai
  // `mode: 'no-cors'` + Content-Type text/plain (simple request, tanpa preflight).
  return ContentService.createTextOutput(JSON.stringify({ status: 'OK', message: 'Survey endpoint active' }))
    .setMimeType(ContentService.MimeType.JSON);
}

function getOrCreateSheet() {
  const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
  let sheet = ss.getSheetByName(SHEET_NAME);

  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    // Header row
    const headers = [
      'Timestamp',
      'Role',
      'Location',
      'Motor Brands',
      'Community',
      'Pain: Diagnosis Difficulty',
      'Pain: Cost Transparency',
      'Pain: Workshop Dependency',
      'Pain: Visual Modification',
      'Pain: Wasted Trip',
      'Behavior: First Action',
      'Behavior: Parts Purchase',
      'Behavior: Mod Interest',
      'Behavior: Apps Used',
      'Feature: AI Diagnosis',
      'Feature: 3D Configurator',
      'Feature: Workshop Finder',
      'Feature: Shopee Link',
      'Feature: History Log',
      'WTP: Bengkel Sub',
      'WTP: User Sub',
      'WTP: Listing Fee',
      'WTP: Payment Method',
      'MVP: Willing',
      'MVP: WhatsApp',
      'MVP: Email',
      'MVP: Channel',
      'Feedback: Feature Request',
      'Feedback: Concern',
      'Feedback: Referral',
      'User Agent',
      'Referrer'
    ];
    sheet.getRange(1, 1, 1, headers.length).setValues([headers]).setFontWeight('bold');
    sheet.setFrozenRows(1);
  }

  return sheet;
}

function appendRow(sheet, data) {
  const row = [
    data.submitted_at || new Date().toISOString(),
    data.q_role || '',
    data.q_location || '',
    Array.isArray(data.q_motor_brand) ? data.q_motor_brand.join(', ') : (data.q_motor_brand || ''),
    data.q_community || '',
    data.q_pain_diagnosis || '',
    data.q_pain_cost_transparency || '',
    data.q_pain_dependency || '',
    data.q_pain_visual_mod || '',
    data.q_pain_wasted_trip || '',
    data.q_where_diagnosis || '',
    data.q_parts_buy || '',
    data.q_mod_interest || '',
    Array.isArray(data.q_app_usage) ? data.q_app_usage.join(', ') : (data.q_app_usage || ''),
    data.q_feat_ai_diagnosis || '',
    data.q_feat_3d_config || '',
    data.q_feat_workshop_finder || '',
    data.q_feat_shopee_link || '',
    data.q_feat_history || '',
    data.q_wtp_bengkel_sub || '',
    data.q_wtp_user_sub || '',
    data.q_wtp_listing_fee || '',
    Array.isArray(data.q_payment_method) ? data.q_payment_method.join(', ') : (data.q_payment_method || ''),
    data.q_willing_mvp || '',
    data.q_contact_wa || '',
    data.q_contact_email || '',
    Array.isArray(data.q_preferred_channel) ? data.q_preferred_channel.join(', ') : (data.q_preferred_channel || ''),
    data.q_feature_request || '',
    data.q_concern || '',
    data.q_referral || '',
    data.user_agent || '',
    data.referrer || ''
  ];

  sheet.appendRow(row);
}

// Helper: Test function (jalankan manual di Apps Script editor)
function testSubmit() {
  const testData = {
    submitted_at: new Date().toISOString(),
    q_role: 'Pemilik motor (pribadi)',
    q_location: 'Bandung',
    q_motor_brand: ['Honda', 'Yamaha'],
    q_community: 'Ya, aktif (Thailook, Bratstyle, Cafe Racer, dll)',
    q_pain_diagnosis: 4,
    q_pain_cost_transparency: 5,
    q_pain_dependency: 3,
    q_pain_visual_mod: 4,
    q_pain_wasted_trip: 2,
    q_where_diagnosis: 'Tanya di grup komunitas/WhatsApp',
    q_parts_buy: 'Shopee/Tokopedia/Lazada',
    q_mod_interest: 'Cukup tertarik (kadang modif ringan)',
    q_app_usage: ['Shopee/Tokopedia (beli suku cadang)', 'Komunitas WhatsApp/Telegram'],
    q_feat_ai_diagnosis: 5,
    q_feat_3d_config: 4,
    q_feat_workshop_finder: 5,
    q_feat_shopee_link: 3,
    q_feat_history: 4,
    q_wtp_bengkel_sub: 'Tidak mau bayar (cuma fitur gratis)',
    q_wtp_user_sub: 'Rp 25.000 – 50.000/bulan',
    q_wtp_listing_fee: '',
    q_payment_method: ['E-wallet (GoPay, OVO, Dana, ShopeePay)', 'ShopeePay (karena sudah beli di Shopee)'],
    q_willing_mvp: 'Ya, sangat bersedia',
    q_contact_wa: '081234567890',
    q_contact_email: 'test@example.com',
    q_preferred_channel: ['WhatsApp Group', 'Telegram Group'],
    q_feature_request: 'Jadwal servis otomatis berdasarkan km',
    q_concern: 'Takut AI salah diagnosis safety-critical part',
    q_referral: 'Bengkel Jaya Motor, Jl. Cihampelas, Pak Budi (0812-xxx-xxxx)',
    user_agent: 'Mozilla/5.0 (test)',
    referrer: 'direct'
  };

  const sheet = getOrCreateSheet();
  appendRow(sheet, testData);
  Logger.log('Test row appended');
}

// Helper: Setup trigger untuk notifikasi email (opsional)
function setupEmailNotification() {
  // Hapus trigger lama
  const triggers = ScriptApp.getProjectTriggers();
  triggers.forEach(t => {
    if (t.getHandlerFunction() === 'onFormSubmit') ScriptApp.deleteTrigger(t);
  });

  // Buat trigger baru
  ScriptApp.newTrigger('onFormSubmit')
    .forSpreadsheet(SpreadsheetApp.openById(SPREADSHEET_ID))
    .onFormSubmit()
    .create();
}

function onFormSubmit(e) {
  // Kirim email notifikasi ke tim (opsional)
  const recipient = 'tim@otomotifvisual3d.com'; // Ganti
  const subject = '📋 Survei Baru: Otomotif Visual 3D';
  const body = `
Survei baru diterima:

Role: ${e.namedValues['Role']?.[0] || '-'}
Lokasi: ${e.namedValues['Location']?.[0] || '-'}
Email: ${e.namedValues['MVP: Email']?.[0] || '-'}
WA: ${e.namedValues['MVP: WhatsApp']?.[0] || '-'}
MVP Willing: ${e.namedValues['MVP: Willing']?.[0] || '-'}

Lihat spreadsheet: https://docs.google.com/spreadsheets/d/${SPREADSHEET_ID}/edit
  `;

  MailApp.sendEmail({ to: recipient, subject, body });
}
