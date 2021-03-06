# Generated by Django 2.2 on 2021-02-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personel_adi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ülke', models.CharField(blank=True, choices=[('TURKIYE', 'Türkiye'), ('GERMANY', 'Almanya'), ('FRANCE', 'Fransa')], max_length=50, null=True)),
                ('bolge', models.CharField(max_length=50)),
                ('firma', models.CharField(max_length=200)),
                ('proje_adi', models.CharField(max_length=200)),
                ('proje_turu', models.CharField(max_length=50)),
                ('kod', models.CharField(max_length=4)),
                ('proje_suresi', models.CharField(blank=True, max_length=10, null=True)),
                ('adres', models.TextField()),
                ('telefon', models.CharField(max_length=15)),
                ('faks', models.CharField(max_length=15)),
                ('genel_mudur', models.CharField(blank=True, max_length=50, null=True, verbose_name='Genel Müdür')),
                ('proje_direktoru', models.CharField(blank=True, max_length=50, null=True)),
                ('proje_muduru', models.CharField(blank=True, max_length=50, null=True)),
                ('proje_mudur_yrd', models.CharField(blank=True, max_length=50, null=True)),
                ('santiye_sefi', models.CharField(blank=True, max_length=50, null=True)),
                ('teknik_ofis_muduru', models.CharField(blank=True, max_length=50, null=True)),
                ('teknik_ofis_elemani', models.CharField(blank=True, max_length=50, null=True)),
                ('dizayn_ofis_sefi', models.CharField(blank=True, max_length=50, null=True)),
                ('planlama_sefi', models.CharField(blank=True, max_length=50, null=True)),
                ('butce_kontrol_muduru', models.CharField(blank=True, max_length=50, null=True)),
                ('ince_isler_sefi', models.CharField(blank=True, max_length=50, null=True)),
                ('elektromekanik_muduru', models.CharField(blank=True, max_length=50, null=True)),
                ('mekanik_isler_sefi', models.CharField(blank=True, max_length=50, null=True)),
                ('elektrik_isler_sefi', models.CharField(blank=True, max_length=50, null=True)),
                ('idari_isler_sefi', models.CharField(blank=True, max_length=50, null=True)),
                ('altyapi_isler_sefi', models.CharField(blank=True, max_length=50, null=True)),
                ('ihale_ve_sozlesme_uzmani', models.CharField(blank=True, max_length=50, null=True)),
                ('maliyet_kontrol_sorumlusu', models.CharField(blank=True, max_length=50, null=True)),
                ('kalite_kontrol_muhendisi', models.CharField(blank=True, max_length=50, null=True)),
                ('finans_muduru', models.CharField(blank=True, max_length=50, null=True)),
                ('muhasebe_muduru', models.CharField(blank=True, max_length=50, null=True)),
                ('muhasebe_sorumlusu', models.CharField(blank=True, max_length=50, null=True)),
                ('insan_kaynaklari', models.CharField(blank=True, max_length=50, null=True)),
                ('satinalma_genel_muduru', models.CharField(blank=True, max_length=50, null=True)),
                ('satinalma_muduru', models.CharField(blank=True, max_length=50, null=True)),
                ('merkez_satinalma_sorumlusu1', models.CharField(blank=True, max_length=50, null=True)),
                ('merkez_satinalma_sorumlusu2', models.CharField(blank=True, max_length=50, null=True)),
                ('santiye_satinalma_sorumlusu1', models.CharField(blank=True, max_length=50, null=True)),
                ('santiye_satinalma_sorumlusu2', models.CharField(blank=True, max_length=50, null=True)),
                ('depo_sorumlusu', models.CharField(blank=True, max_length=50, null=True)),
                ('depo_elemani', models.CharField(blank=True, max_length=50, null=True)),
                ('proje_personeli', models.ManyToManyField(null=True, to='projects_api.Personel')),
            ],
        ),
    ]
